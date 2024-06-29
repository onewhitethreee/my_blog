---
title: Windows应用开机自启动_Flutter
layour: post
uuid: fswt2d-arr-11ed-fasfw-wqr2fg
tags: [Flutter, Windows]
categories: Flutter
date: 2024-06-29 18:07:08
---

当个备忘录给自己看，大佬看见了别嘲笑。

---

一个windows软件想要开机自启有好几种方案，注册表，放入自启动文件夹..

这里我选择的是注册表，相关的注册表为 HKEY_CURRENT_USER `'Software\\Microsoft\\Windows\\CurrentVersion\\Run'`。想要软件开机自启动只需要在这里写入你的软件名字和软件目录。

---


微软已经写好了相关的函数，我直接就拿来调用了。是一个叫做 RegSetValueExA的函数在 (winreg.h)有定义，需要传入几个参数。

```
LSTATUS RegSetValueExA(
  [in]           HKEY       hKey, 
  [in, optional] LPCSTR     lpValueName,
                 DWORD      Reserved,
  [in]           DWORD      dwType,
  [in]           const BYTE *lpData,
  [in]           DWORD      cbData
);
```


相关的文档可以在[这里看](https://learn.microsoft.com/zh-cn/windows/win32/api/winreg/nf-winreg-regsetvalueexa#requirements)。
---

这里我就不讨论了，我来研究在flutter中应该怎么去调用这个库。很幸运的是，已经有大佬写好了，我也是直接拿来调用就ok了。

首先要导入一些包
```
import 'dart:ffi';
import 'package:win32/win32.dart';
import 'package:ffi/ffi.dart';
```
然后去调用RegSetValueEx这个函数，跟上面微软的是一样的。这里直接贴出代码

```
void enableStartUpOnWindows() {
    final hkey = HKEY_CURRENT_USER;
    final lpSubKey =
        'Software\\Microsoft\\Windows\\CurrentVersion\\Run'.toNativeUtf16();
    final dwType = REG_VALUE_TYPE.REG_SZ;
    final programName = 'My program'.toNativeUtf16();
    final lpData = Platform.resolvedExecutable.toNativeUtf16();

    final phkResult = calloc<HKEY>();

    try {
      final lResult = RegOpenKeyEx(
        hkey,
        lpSubKey,
        0,
        REG_SAM_FLAGS.KEY_SET_VALUE,
        phkResult,
      );

      if (lResult == WIN32_ERROR.ERROR_SUCCESS) {
        final setResult = RegSetValueEx(
          phkResult.value,
          programName,
          0,
          dwType,
          lpData.cast<Uint8>(),
          lpData.length * 2, // 写入的方式是char，1 char = 2 bits
        );

        if (setResult != WIN32_ERROR.ERROR_SUCCESS) {
          throw WindowsException(setResult);
        }
      } else {
        throw WindowsException(lResult);
      }
    } finally {
      if (phkResult.value != NULL) {
        RegCloseKey(phkResult.value);
      }
      free(phkResult); // 释放一下申请的内存
      free(lpSubKey);
      free(programName);
      free(lpData);
    }
  }
```

然后就是禁止开机自启的内容。
---

也是直接拿来用，有人已经写好了。

跟开机开启的逻辑一样，不过不同的是一个是写入另外一个是删除。

代码
```
void disableStartUpOnWindows() {
    final hkey = HKEY_CURRENT_USER;
    final lpSubKey =
        'Software\\Microsoft\\Windows\\CurrentVersion\\Run'.toNativeUtf16();
    final programName = 'My program'.toNativeUtf16();

    final phkResult = calloc<HKEY>();

    try {
      final lResult = RegOpenKeyEx(
        hkey,
        lpSubKey,
        0,
        REG_SAM_FLAGS.KEY_SET_VALUE,
        phkResult,
      );

      if (lResult == WIN32_ERROR.ERROR_SUCCESS) {
        final deleteResult = RegDeleteValue(
          phkResult.value,
          programName,
        );

        if (deleteResult != WIN32_ERROR.ERROR_SUCCESS) {
          throw WindowsException(deleteResult);
        }
      } else {
        throw WindowsException(lResult);
      }
    } finally {
      if (phkResult.value != NULL) {
        RegCloseKey(phkResult.value);
      }
      free(phkResult);
      free(lpSubKey);
      free(programName);
    }
  }
```
---

完毕
