*** Settings ***
Documentation    This file contains test cases to validate the automation by template matching methods

Resource    ../resource/common.resource

Test Setup    StartTest
#Test Teardown    EndTest

*** Test Cases ***
AppleTest
   
    ClickBuy    MacBook Air
    
    ClickSelect
    
    SeeDeliveryOptions    500079
    #"Here cant find the xpath for search icon to click for search execution hence here we can use use ml method"
    

    AddToBag
    #"Here cant find the xpath for search icon to click for search execution hence here we can use use ml method" 
     
    ClickCart
    #"Here cant find the xpath for search icon to click for search execution hence here we can use use ml method"
    
    ClickRemove