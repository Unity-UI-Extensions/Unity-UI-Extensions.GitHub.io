---
layout: control-ugui
title: "UI Line Connector"
description: "Draws connecting lines between RectTransform anchors with configurable width."
category: "Primitives"
permalink: /ugui/controls/ui-line-connector/
has_video: true
tags: [primitives, line, connector, link, bezier]
---
# UILineConnector

A Line Renderer helper used to draw a chain between multiple gameObjects, like a node connector

<!--![](/ugui/images/ Game Image.jpg)-->

---------

## Contents

> 1 [Overview](#overview)
>
> 2 [Properties](#properties)
>
> 3 [Methods](#methods)
>
> 4 [Usage](#usage)
>
> 5 [Video Demo](#video-demo)
>
> 6 [See also](#see-also)
>
> 7 [Credits and Donation](#credits-and-donation)
>
> 8 [External links](#external-links)

---------

## Overview

The UI Line Connector, allows you Override the Line Renderer control to build a line connecting the selected GameObjects.

![](/ugui/images/UILineConnectorInspector.jpg)

This produces a Node connector style effect between the provided UI GameObjects.

![](/ugui/images/UILineConnectorSample.jpg)

> [!NOTE]
> Depends on the [UI Line Renderer](/ugui/controls/ui-line-renderer/) component

> [!NOTE]
> The Lines depend on the Pivot's of the Main Canvas, Line Renderer and the Selected GameObjects.  Adjust as required.
---------

## Properties

The properties of the UILineConnector control are as follows:

Property | Description
-|-
*Transforms*|The List of GameObjects to connect lines between

### Requires Line Renderer Component

---------

## Methods

This component does not expose public methods beyond inherited behaviour.

---------

## Usage

The UILineConnector is available using:

"Add Component -> UI -> Extensions -> UI Line Connector"

This will also add the [UI Line Renderer](/ugui/controls/ui-line-renderer/) component by default

---------

## Video Demo

<video class="demo-video" controls preload="metadata" loop muted playsinline poster="/ugui/images/UILineConnectorDemo.jpg" aria-label="UI Line Connector demo">
  <source src="/ugui/images/UILineConnectorDemo.webm" type="video/webm">
</video>

---------

## See also

* [UILineRenderer](/ugui/controls/ui-line-renderer/)

---------

## Credits and Donation

Credit [Alastair Aitchison](https://bitbucket.org/alastaira/)

---------

## External links

Sourced from - [https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/123/uilinerenderer-issues-with-specifying
](https://bitbucket.org/UnityUIExtensions/unity-ui-extensions/issues/123/uilinerenderer-issues-with-specifying
)
