# Preparation Issues

* The first issue I encountered was having to analyze the original csv 
  transcript and see what each column represented. From there I had to 
  think about which column mapped to each of: episode, speaker, content.


* The second issue I faced was with modifying the content so that it 
  only contained spoken text. At first, I tried to remove the brackets, 
  but that wasn't enough because I saw that some lines contained some 
  weird text like this: <...>, so I had to go back and remove that too.


* The third issue I faced was figuring out what should be considered 
  spoken text. I was unsure whether some things like ... or --- in 
  between other letters should count as spoken text. In the end I 
  decided to keep these.