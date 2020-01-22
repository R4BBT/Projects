# To begin: Type robot NewOne.robot
*** Settings ***
Documentation    Suite description
Library  SeleniumLibrary


*** Variables ***
${Browser}  chrome
${Url}  https://demo.nopcommerce.com/


*** Test Cases ***
LoginTest
     open browser  ${URL}  ${browser}
     LoginToApplication
     close browser

*** Keywords ***
LoginToApplication
     click link  xpath://a[@class='ico-login']
     input text  id:Email  pavanoltraining@gmail.com
     input text  id:Password  Test@123
     click element  xpath://input[@class='button-1 login-button']