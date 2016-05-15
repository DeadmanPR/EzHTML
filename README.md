# Brief Introduction
Since the development of the internet, technology has become an important part of our lives. For that reason, web pages are used daily in order to facilitate and organize information, social interactions, online shopping, along many other activities. Therefore to create a web page, people must learn programming languages like HTML/CSS. Because of the need of people with HTML/CSS knowledge, we found the motivation for developing an intuitive language, called EzHTML, that can make it easy for those that may have difficulties learning HTML/CSS. Our objective is to develop a clearer and simpler language so that the user doesn't have to go through the tedious and/or exhausting process of opening and closing HTML tags (<> | </>), increasing readability of the code and saving some coding time. 

# EzHTML

EzHTML is a programming language that helps people create web pages (or websites). It offers a syntax similar to C/C++, so that people that know these languages can easily grasp EzHTML's syntax. 

## Features
This language handles the following HTML/CSS functionality:
- Webpage Title
- Background Color
- Headings (h1 to h6)
  - Color
  - Alignment
  - Font
  - Font Size
  - Bold/Italic/Underline
- Paragraphs
  - Color
  - Alignment
  - Font
  - Font Size
  - Bold/Italic/Underline

- Hyperlinks (Links)
  - Text to be shown as the link
  - Alignment
  - Font Size
 
- Images
  - Image width and height
  - Image link destination (when

Note: This project was developed using Python Lex-Yacc (PLY for short). Therefore, you must have Python 2.7 installed on your computer.


# How to execute the test program provided:
    1- Download the project as a ZIP file, and extract it somewhere on your 
    computer.
    2- Open your terminal, locate the folder to which you extracted the ZIP
    file.
    3- Type "python myParse.py"
    4- The parser will start executing and will ask you for the name of the 
    source code file.
    5- Since this is a test program, type "sourceCode" and hit the <Enter>
    key. You can type any file name, as long as it has valid EzHTML syntax.
    6- If everything worked correctly, the website should open up in your
    default internet browser.

# Syntax
As previously mentioned, EzHTML's syntax is similar to C/C++. Every statement must be followed by a semicolon [ ; ]. Here's a brief description of the syntax.

### Title and Body Statements
Every EzHTML program must have these two keywords: Title and Body. 
##### Title
In order to set a title for your webpage, you must follow the following syntax:
```C
TITLE = "Webpage Title";
```
Note that the title is between quotation marks [ " " ] since it is essentially a group of characters (similar to how Strings are written in C/C++).
##### Body
After the title has been set, your whole program resides in a _body_ block. Think of it as the ```main()``` function of every C/C++ program.
``` C
body{
    //Program goes here
};
```
Note that a semicolon [ ; ] follows the closing bracket [ } ]. As with every statement, this must be done.

### Background Color
A background color can be set for the webpage.
```C
body{
    BACKGROUND_COLOR = BLUE;
};
```
Note that the value is written in capital letters (similar to how constants are used in C/C++) and with no quotation marks. 

A list of possible values can be found here: http://www.w3schools.com/colors/colors_names.asp

### Headings
Adding a heading to your webpage is simple. It follows the following syntax:
```C
body{
    heading1 firstHeader = "Heading1!";
    heading2 he2 = "Heading1!";
    heading3 numberThree = "Heading1!";
    heading4 a1337hax = "Heading1!";
    heading5 a = "Heading1!";
    heading6 yep = "Heading1!";
};
```
A heading declaration must start with the type of heading (_heading1_ to _heading6_), followed by an identifier (a letter followed by letters or numbers) and assigning a text value using the equal sign.

##### Heading Style
You can set certain attributes of a heading. These are its color, alignment, font, font-size, and if it is bold, underlined or italic. 
```C
body{
    heading1 h1 = "Test";
    style(h1){
        color = WHITE;
		alignment = CENTER;
		font = COURIER;
		font-size = 12;
		isBold = FALSE;     //Possible values: TRUE or FALSE
		isItalic = TRUE;
		isUnderline = TRUE;
	};
}:
```
Note: All attributes ***must*** be present in the heading style definition (in other words, omitting the color attribute will result in an error).

### Paragraphs
To add a paragraph to your webpage, it follows the following pattern:
```C
body{
    paragraph firstPar = "This is the content of the paragraph";
};
```

Paragraphs follow a syntax similar to the headings previously mentioned. To create a paragraph, the keyword _paragraph_ must be present. After the keyword, an identifier is used and assigned a text value using the equal sign.

##### Paragraph Style
Paragraphs also have attributes that can be modified. These are the same as the heading attributes, and is written in a similar fashion:
```C
body{
    paragraph p1 = "Testing with a paragraph!";
    style(p1){
        color = BLUE;
		alignment = CENTER;
		font = COURIER;
		font-size = 18;
		isBold = TRUE;     //Possible values: TRUE or FALSE
		isItalic = FALSE;
		isUnderline = FALSE;
	};
}:
```

### Hyperlinks (Links)
Links have a different syntax to the elements seen so far. This time, a `link` variable is declared, and its attributes are set directly following it.
```C
body{
    link myLink;
    linkAttr(myLink){
        destination = "http://www.google.com";
        text = "Go to Google!";
        alignment = CENTER;
        font-size = 144;
    };
};
```

Links have four attributes to be defined:
- destination -> the webpage to open when the link is clicked
- text -> the text to show as the link that can be clicked
- aligment -> alignment of the link on the webpage
- font-size -> the font size of the text

### Images
Images follow a similar pattern to how links are created. An `image` variable is declared, and its attributes definition immediately follows it.
```C
body{
    image myImage;
    imageAttr(myImage){
		source = "http://xiostorage.com/wp-content/uploads/2015/10/test.png";
		height = 200;
		width = 200;
		destination = "None";
	};
};
```

Images have four attributes to be set:
- source -> the source of the image (can be local [ex. `"images/test.png"`] or a link
- height -> the desired height of the image
- width -> the desired width of the image
- destination -> distinguishes if the image is a link as well [ex. `destination = "http://www.uprm.edu";`] or if the image is not a link [ex. `destination = "None";`]


### Comments
Comments are ignored by the program itself, but helps increase the code readability. Any line that starts with two forward slashes [ // ] will be treated as a comment.

Single Line Comments:
```C
...
//This is a comment
...
```

Multi-Line Comments:
``` C
...
//This is
//a multi-line
//comment
...
```

    
