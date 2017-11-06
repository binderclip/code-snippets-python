# 把 CMYK 模式的图片转换为 RGB 模式

- Finder 和预览打开 CMYK 的图片颜色正常
- Chrome 中显示 CMYK 的图片颜色异常
- Photoshop 转换完的效果是正常的，不过 CMYK 到 RGB 再转换回 CMYK 颜色会发生一点变化
- 未设置 icc 的时候直接用 Pillow 转换图片到 RGB 的效果和浏览器中异常的效果几乎一样
- 设置对应的 icc 后转换出来的是接近正常的

ref:

- [python - Conversion from CMYK to RGB with Pillow is different from that of Photoshop - Stack Overflow](https://stackoverflow.com/questions/38855022/conversion-from-cmyk-to-rgb-with-pillow-is-different-from-that-of-photoshop)
- [Pillow — Pillow (PIL Fork) 4.4.0.dev0 documentation](http://pillow.readthedocs.io/en/latest/)
- [ICC profile downloads - Mac](http://www.adobe.com/support/downloads/iccprofiles/iccprofiles_mac.html)
- [sRGB Color Space Profile.ICM](https://github.com/xorgy/graphicsmagick/blob/master/profiles/sRGB%20Color%20Space%20Profile.ICM)
