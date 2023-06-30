# gta-v-tunables-tracker

A GitHub Actions-powered scraper for the GTA V tunables file.

---

The tunables file, originally known as `tunables.json` and now
`0x1a098062.json`, is used to configure global properties in the otherwise
peer-to-peer game of GTA Online. The tunables are mainly used to toggle
features like seasonal effects and adjust game objectives, though
[the PC tunables file is also used to distribute anti-cheat configurations](https://github.com/yubie-re/gtav-sigscan).
The tunables file is streamed to players as an encrypted blob when they
initiate an online connection.

This repo is automatically updated every hour and tracks changes to the
tunables file for each platform:

|Platform|`tunables.json`|Last Update|Number of Logged Updates|
|-|-|-|-|
|PC|[`tunables-pcros.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-pcros.json)|`2023-06-29T08-50-34`|[164](https://github.com/branw/gta-v-tunables-tracker/blob/main/changelog-pcros.md)|
|Xbox Series X|[`tunables-xboxsx.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-xboxsx.json)|`2023-06-30T15-53-05`|[102](https://github.com/branw/gta-v-tunables-tracker/blob/main/changelog-xboxsx.md)|
|Xbox One|[`tunables-xboxone.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-xboxone.json)|`2023-06-29T08-48-32`|[96](https://github.com/branw/gta-v-tunables-tracker/blob/main/changelog-xboxone.md)|
|Xbox 360|[`tunables-xbox360.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-xbox360.json)|`2019-12-05T23-32-04`|0[^1]|
|PS5|[`tunables-ps5.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-ps5.json)|`2023-06-30T15-53-15`|[101](https://github.com/branw/gta-v-tunables-tracker/blob/main/changelog-ps5.md)|
|PS4|[`tunables-ps4.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-ps4.json)|`2023-06-29T08-46-48`|[97](https://github.com/branw/gta-v-tunables-tracker/blob/main/changelog-ps4.md)|
|PS3|[`tunables-ps3.json`](https://github.com/branw/gta-v-tunables-tracker/blob/main/tunables-ps3.json)|`2019-12-05T23-30-17`|0[^1]|

Historical entries can be found in [`history/`](https://github.com/branw/gta-v-tunables-tracker/blob/main/history).

[^1]: [GTA Online for the Xbox 360 and PS3 was shutdown in December 2021](https://www.rockstargames.com/newswire/article/51989315o2aa3a/gta-online-for-playstation-3-and-xbox-360-will-shut-down-on-december-1),
so these files are not expected to receive any further updates.

## License

> This is free and unencumbered software released into the public domain.
> 
> Anyone is free to copy, modify, publish, use, compile, sell, or
> distribute this software, either in source code form or as a compiled
> binary, for any purpose, commercial or non-commercial, and by any
> means.
> 
> In jurisdictions that recognize copyright laws, the author or authors
> of this software dedicate any and all copyright interest in the
> software to the public domain. We make this dedication for the benefit
> of the public at large and to the detriment of our heirs and
> successors. We intend this dedication to be an overt act of
> relinquishment in perpetuity of all present and future rights to this
> software under copyright law.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
> IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
> OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
> ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
> OTHER DEALINGS IN THE SOFTWARE.
> 
> For more information, please refer to <https://unlicense.org>
