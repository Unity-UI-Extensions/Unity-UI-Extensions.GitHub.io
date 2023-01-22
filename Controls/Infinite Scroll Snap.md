This is a code I wrote to add snap functionality to UI_InfiniteScroll. I've only tested it in vertical, but it should work perfectly fine horizontally as well. Feel free to add this to your projects and really do anything with it. Forgive me I don't really know how bitbucket works, and this is really the only place I could find to insert my code.
```
#!c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UI.Extensions;
using UnityEngine.EventSystems;

public class UI_InfiniteScrollSnap : MonoBehaviour, IBeginDragHandler, IEndDragHandler
{
    //this component is meant to be added to objects which have UI_InfiniteScroll components
    //if true user will need to call Init() method manually (in case the contend of the scrollview is generated from code or requires special initialization)
    [Tooltip("If false, will Init automatically, otherwise you need to call Init() method")]
    public bool InitByUser = false;
    public RectTransform _center; //the transform target of lerping. the list item closest to this recttransform is the 'center' of it

    private UI_InfiniteScroll _UI_InfiniteScroll;
    private ScrollRect _scrollRect;
    private RectTransform _content;
    private RectTransform _centerChild; //the closest child to the center
    public RectTransform CenterChild //the center child needs to be initialized as to begin with
    {
        set { _centerChild = value; }
    }
    private bool _centerChildChanged; //if the closest child to the center has changed
    private bool _beingDragged;
    private bool _isLerping;

    private int dragCheck;

    void Awake()
    {
        if (!InitByUser)
        {
            Init();
        }
    }
    public void Init()
    {
        if (_snapRecieverGameObject != null)
        {
            _snapReciever = _snapRecieverGameObject.GetComponent<IRecievesSnap>();
        }
        if (GetComponent<UI_InfiniteScroll>() != null)
        {
            _UI_InfiniteScroll = GetComponent<UI_InfiniteScroll>();
            if (GetComponent<ScrollRect>() != null)
            {
                _scrollRect = GetComponent<ScrollRect>();
                _content = _scrollRect.content;
            }
        }
    }
    public void Update()
    {
        if (_isLerping)
        {
            if (_centerChild.position.Equals(_center.position)) _isLerping = false;
            else
            {
                _content.transform.position -= MyMath.Lerp(Vector3.zero, _centerChild.position - _center.position, .2f);
            }

        }
        else if (_scrollRect.velocity.y < 30f) //if the list is being scrolled slowly
        {
            foreach (RectTransform child in _content) //this for loop finds the closest child to the center
            {
                if ((child.position - _center.position).magnitude < (_centerChild.position - _center.position).magnitude)
                {
                    _centerChild = child;
                    _centerChildChanged = true;
                }
            }
            if (_centerChildChanged)
            {
                _snapReciever.Recieve(_centerChild); //the menu which will recieve the message that this child is the new focus of the menu
                _centerChildChanged = false;
            }
            if (!_isLerping && !_beingDragged && (_scrollRect.velocity).magnitude < 20) //if the menu is moving really slowly, it should lerp to the center
            {
                _scrollRect.velocity = Vector3.zero;
                _isLerping = true;
            }
        }
    }

    public void OnBeginDrag(PointerEventData eventData)
    {
        _beingDragged = true;
        _isLerping = false;
    }

    public void OnEndDrag(PointerEventData eventData)
    {
        _beingDragged = false;
    }
}

```