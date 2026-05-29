# Input Field Enter Submit

A simple utility component that automatically submits an InputField when the Enter key is pressed.

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

InputFieldEnterSubmit is a lightweight utility component that extends the standard Unity InputField with automatic submission on Enter key press. When the Enter key is pressed (or Enter on the numeric keypad), the component:

1. Triggers the `EnterSubmit` event with the current input text
2. Optionally defocuses the input field (clears selection)

This is useful for creating form-like interactions where pressing Enter should submit data (search boxes, chat input, command prompts, etc.).

---------

## Properties

The properties of the Input Field Enter Submit control are as follows:

Property | Description
-|-
*Defocus Input*|When true, the InputField loses focus after submission. When false, the field retains focus for further input.
***Enter Submit*** (event)|Event invoked when Enter is pressed, passes the current input text as a string parameter.

---------

## Methods

Method | Arguments | Description
-|-|-
*OnEndEdit*|txt (string)|Internal method called by InputField's onEndEdit event. Checks for Enter key press and invokes EnterSubmit event.

---------

## Usage

Add the Input Field Enter Submit component to the same GameObject as an InputField:

"Add Component -> UI -> Extensions -> Input Field Submit"

The component will automatically detect the InputField on the same GameObject.

### Basic Usage

```csharp
public InputFieldEnterSubmit inputField;

void Start()
{
    // Listen for Enter key submission
    inputField.EnterSubmit.AddListener(OnInputSubmitted);
}

void OnInputSubmitted(string input)
{
    Debug.Log("User submitted: " + input);
}
```

### Search Box Example

```csharp
public InputFieldEnterSubmit searchField;
public Text resultsText;

void Start()
{
    searchField.defocusInput = true;  // Clear focus after search
    searchField.EnterSubmit.AddListener(OnSearch);
}

void OnSearch(string query)
{
    // Perform search with the query
    var results = SearchDatabase(query);
    resultsText.text = "Found " + results.Count + " results";
}
```

### Chat Input Example

```csharp
public InputFieldEnterSubmit chatInput;
public ScrollRect messageScroll;

void Start()
{
    chatInput.defocusInput = false;  // Keep focus for rapid typing
    chatInput.EnterSubmit.AddListener(OnMessageSent);
}

void OnMessageSent(string message)
{
    // Send the message
    SendChatMessage(message);
    
    // Clear for next message
    chatInput.GetComponent<InputField>().text = "";
}
```

### Command Prompt Example

```csharp
public InputFieldEnterSubmit commandInput;

void Start()
{
    commandInput.EnterSubmit.AddListener(OnCommandEntered);
}

void OnCommandEntered(string command)
{
    // Parse and execute command
    ExecuteCommand(command);
}

void ExecuteCommand(string command)
{
    string[] parts = command.Split(' ');
    string action = parts[0];
    
    switch (action)
    {
        case "help":
            Debug.Log("Available commands: help, load, save, exit");
            break;
        case "load":
            LoadGame(parts.Length > 1 ? parts[1] : "");
            break;
        case "save":
            SaveGame(parts.Length > 1 ? parts[1] : "");
            break;
    }
}
```

### Controlling Defocus Behavior

```csharp
public InputFieldEnterSubmit inputField;
private bool shouldFocusAfterSubmit;

void Start()
{
    inputField.EnterSubmit.AddListener(OnSubmit);
}

void OnSubmit(string text)
{
    ProcessInput(text);
    
    // Optionally defocus based on some condition
    if (shouldFocusAfterSubmit)
    {
        inputField.defocusInput = false;
    }
    else
    {
        inputField.defocusInput = true;
    }
}
```

### Using with Multiple InputFields

```csharp
public InputFieldEnterSubmit[] formFields;

void Start()
{
    foreach (var field in formFields)
    {
        field.EnterSubmit.AddListener(OnFieldSubmitted);
    }
}

void OnFieldSubmitted(string value)
{
    // Process submission - context comes from which field was submitted
    Debug.Log("Field submitted: " + value);
}
```

---------

## Video Demo

Coming soon...

---------

## See also

* [InputFocus](/Controls/InputFocus.md)
* [ReturnKeyTrigger](/Controls/ReturnKeyTrigger.md)
* [Stepper](/Controls/Stepper.md)

---------

## Credits and Donation

Vicente Russo

---------

## External links

[Sourced from](https://bitbucket.org/SimonDarksideJ/unity-ui-extensions/issues/23/returnkeytriggersbutton)
[Unity InputField Documentation](https://docs.unity3d.com/Manual/script-InputField.html)
