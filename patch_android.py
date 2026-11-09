"""Run after `npx cap add android`: adds storage permissions + legacy storage flag to the manifest."""
import re
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf8").read()
perms = [
  '<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />',
  '<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="32" />',
  '<uses-permission android:name="android.permission.USE_BIOMETRIC" />',
]
for x in perms:
    name = re.search(r'android:name="([^"]+)"', x).group(1)
    if name not in s:
        s = s.replace("<application", x + "\n    <application", 1)
if "requestLegacyExternalStorage" not in s:
    s = s.replace("<application", '<application android:requestLegacyExternalStorage="true"', 1)
open(p, "w", encoding="utf8").write(s)
print("manifest patched")
