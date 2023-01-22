# CLFZ2 - LFZ Compression helper

==============

LZF Compression library to compress data

---------

## Contents

> 1 [Overview](#markdown-header-overview)

> 2 [Usage](#markdown-header-usage)

> 3 [Video Demo](#markdown-header-video-demo)

> 4 [See also](#markdown-header-see-also)

> 5 [Credits and Donation](#markdown-header-credits-and-donation)

> 6 [External links](#markdown-header-external-links)

---------

## Overview

The LZF Compression component is a useful extension to Unity to be able to compress data for sending over a network or for more efficient saving.

The library is complete and has even been patched a few times already through the forum thread, so I took the most stable version without issues. (issus were reported on other versions, so I didn't take them)

There are some Unit Tests included in the following file:
>Assets\unity-ui-extensions\Scripts\Editor\CompressionTests.cs

These details some sample use cases and also provide a good way to test that the compression/decompression works as expected.
To run these Unit Tests In Unity 5.3, open the following editor window from the menu to see the tests and run them.
>Window\Editor Tests Runner

(For earlier versions of Unity, you will need to install the "Unity Test Tools" asset from the store and follow the instructions from there.)

---------

## Usage

Simply create a byte array in code for the data you want compressed and pas it to the Compress function of the Library, as follows:

```csharp
      byte[] byteText = Encoding.Unicode.GetBytes(x);
      var compressed = CLZF2.Compress(byteText);
```

To decompress, follow the same process using the Decompress function and then unencode your data as follows:

```csharp
      var decompressed = CLZF2.Decompress(compressed);
      var outString = Encoding.Unicode.GetString(decompressed);
```

For more examples, see the Unit Tests included in the following file:
>Assets\unity-ui-extensions\Scripts\Editor\CompressionTests.cs

---------

## Video Demo

N/A

---------

## See also

N/A

---------

## Credits and Donation

Roman Atachiants <kelindar@gmail.com>
Oren J. Maurice <oymaurice@hazorea.org.il>
Marc Alexander Lehmann <schmorp@schmorp.de>

---------

## External links

[Sourced From](http://forum.unity3d.com/threads/lzf-compression-and-decompression-for-unity.152579/)
