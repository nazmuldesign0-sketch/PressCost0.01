"""Native splash (Android 12+) = plain green, so only our 3-second PressCost splash is visible."""
import pathlib
p = pathlib.Path("android/app/src/main/res/values/styles.xml")
s = p.read_text(encoding="utf-8")
marker = '<style name="AppTheme.NoActionBarLaunch"'
if "windowSplashScreenBackground" not in s and "Theme.SplashScreen" in s and marker in s:
    i = s.index(marker); j = s.index(">", i) + 1
    add = ('\n        <item name="windowSplashScreenBackground">#71BF45</item>'
           '\n        <item name="windowSplashScreenAnimatedIcon">@android:color/transparent</item>')
    s = s[:j] + add + s[j:]
    p.write_text(s, encoding="utf-8")
    print("styles.xml patched")
else:
    print("styles.xml left unchanged")
