*** Settings *** 

Documentation    This file will take care of configuration such as broweser activities,
...    screenshot folder and keywords for automation

Library    SeleniumLibrary    screenshot_root_directory=screenshot        
Library    OperatingSystem     
#Library    MLPython.py 
Library    Temp.py    

*** Variables ***

${BROWSER NAME}    chrome
${URL}    https://www.apple.com/in/
${SCREENSHOT}    D:\\main\\xda.png

*** Keywords ***
*** Keywords ***
StartTest
    Append To Environment Variable    Path   ${EXECDIR}${/}driver${/} 
    Open Browser    browser=${BROWSER NAME}
    Maximize Browser Window
    Go To    url=${URL}    
    Set Browser Implicit Wait    10s
    
EndTest
    Close Browser
    
    
ClickBuy
    [Arguments]    ${value}
    Wait Until Element Is Visible    //a[contains(@class,'icon icon-after icon-chevronright')]//following::*[contains(@data-analytics-title,'Buy ${value}')]
    Sleep    2s      
    Click Element    //a[contains(@class,'icon icon-after icon-chevronright')]//following::*[contains(@data-analytics-title,'Buy ${value}')]
    Sleep    5s      
    
    
ClickSelect   
    Wait Until Element Is Visible    (//*[contains(@href,"https://www.apple.com/in/macbook-air")])[1]    
    Scroll Element Into View    (//*[@class="as-macbundle column large-4 small-12 as-macbundle-offset2"]//following::*[@class="as-macbundle-actioncontainer"])[1]
    Click Element    (//*[@class="as-macbundle column large-4 small-12 as-macbundle-offset2"]//following::*[@class="as-macbundle-actioncontainer"])[1]    
    

SeeDeliveryOptions
    [Arguments]    ${pincode}    
    Sleep    2s
    Capture Page Screenshot    D:\\main\\xda.png
    sleep    5s
    ${delivery}    delivery
    Log To Console    ${delivery} 
    Sleep    3s   
    Coordinates Click    ${delivery}[0]    ${delivery}[1]  
    Wait Until Element Is Visible    //input[@id='postalCode']    
    Input Text    //input[@id='postalCode']    ${pincode}
    Sleep    2s
    Capture Page Screenshot    D:\\main\\xda.png
    sleep    5s
    ${options}    options
    Log To Console    ${options} 
    Sleep    3s   
    Coordinates Click    ${options}[0]    ${options}[1]  
    Wait Until Element Is Visible    //li[contains(@class,'as-datatable-row as-deliverydatesoverlay-deliveryoptions-list')]    
    ${value}    Get Text    //li[contains(@class,'as-datatable-row as-deliverydatesoverlay-deliveryoptions-list')]
    Log To Console    ${value}    
    Sleep    2s
    Capture Page Screenshot    D:\\main\\xda.png
    sleep    5s
    ${cross}    cross
    Log To Console    ${cross} 
    Sleep    3s   
    Coordinates Click    ${cross}[0]    ${cross}[1]  

    
AddToBag
    Sleep    2s
    Capture Page Screenshot    D:\\main\\xda.png
    sleep    5s
    ${AddToBag}    add
    Log To Console    ${AddToBag} 
    Sleep    3s   
    Coordinates Click    ${AddToBag}[0]    ${AddToBag}[1]  
     
         
 ClickCart
    Sleep    2s
    Capture Page Screenshot    D:\\main\\xda.png
    sleep    5s
    ${cart}    cart
    Log To Console    ${cart} 
    Sleep    3s   
    Coordinates Click    ${cart}[0]    ${cart}[1]  
    Wait Until Element Is Visible    //a[contains(text(),'Bag (1)')]    
    Click Element    //a[contains(text(),'Bag (1)')]    
    Page Should Contain Element    //h1[contains(text(),'Your bag total is ')]       
    
ClickRemove
    Wait Until Element Is Visible    //span[contains(text(),'Remove')]    
    Click Element    //span[contains(text(),'Remove')]   