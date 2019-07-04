import random

possible_titles = ["Welcome", "Getting Started", "Required Environment", "How to Contribute", "Feedback", "Contributing", "Installation", "Building the Project"]

possible_languages = ["Python", "Java", "NodeJs", "Haskell", "Rust", "C", "C++", "Scala", "Ruby", "Fortran", "Lua", "C#"]

language = possible_languages[ random.randint(0,len(possible_languages) - 1) ]

text = {}
text['Welcome'] = []
text['Welcome'].append("These SDKs allow us to create native " + language + " iOS, tvOS, watchOS and macOS applications using the same UI controls we would in Objective-C and Xcode, except with the flexibility and elegance of a modern language (C#), the power of the .NET Base Class Library (BCL), and two first-class IDEs—Visual Studio for Mac and Visual Studio—at our fingertips.")
text['Welcome'].append("This is a " + language + " development platform for building mobile and desktop web applications using Typescript/JavaScript and other languages.")
text['Welcome'].append("Truth makes your test assertions and failure messages more readable. Similar to AssertJ, it natively supports many JDK and Guava types, and it is extensible to others.\n\nTruth is owned and maintained by the Guava team. It is used in the majority of the tests in Google’s own codebase.\n\nRead more at the main website.\n\n")

text["Getting Started"] = []
text["Getting Started"].append("Welcome to " + language + "! \n \n This tutorial introduces you to the essentials of " + language + ". It leverages what you already know about HTML and JavaScript—plus some useful " + language + " features—to build a simple online store application, with a catalog, shopping cart, and check-out form. You don't need to install anything: you'll build the app using the StackBlitz online development environment.")
text["Getting Started"].append("See our documentation on " + language + "io.\n\nTry our interactive tutorial.\n\nTake a free course on Scalable Microservices with " + language)

text["Required Environment"] = []
text["Required Environment"].append("You must set up a MySQL database called 'db', running on localhost, username 'user' with password '123'.  This is required for maximum security")
text["Required Environment"].append("Just copy the .env file from the link given and you're ready to go!")
text["Required Environment"].append("This code is a Windows-only project")

text["How to Contribute"] = []
text["How to Contribute"].append("The community repository hosts all information about building " + language + " from source, how to contribute code and documentation, who to contact about what, etc.\n\nIf you want to build " + language + " right away there are two options:")

text["Feedback"] = []
text["Feedback"].append("Please feel free to go to our forum to leave any feedback")
text["Feedback"].append("Sign up to our mailing list!")


text["Contributing"] = []
text["Contributing"].append("Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our guidelines for contributing and then check out one of our issues in the hotlist: community-help.")

text["Installation"] = []
text["Installation"].append("Just run ./configure, then make, then make install")
text["Installation"].append("Just run npm install, then npm run")
text["Installation"].append("Just run python main.py")

text["Building the Project"] = []
text["Building the Project"].append("The protocol compiler is written in C++. If you are using C++, please follow the C++ Installation Instructions to install protoc along with the C++ runtime.\n\nFor non-C++ users, the simplest way to install the protocol compiler is to download a pre-built binary from our release page:")

output = ""
for n in range(0, random.randint(2,len(possible_titles)-1)):
    title = possible_titles[n]
    output += "# " + title + "\n\n"
    output += text[title][random.randint(0,len(text[title])-1)] + "\n\n"

print (output)
