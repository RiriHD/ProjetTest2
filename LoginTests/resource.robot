*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           OperatingSystem
Library             ${CURDIR}${/}loginTest.py
*** Variables ***
${VALID USER}           agts.etc@gmail.com
${VALID PASSWORD}       AZERTY123
${invalidlog}           inv@gmail.com
${invalidpwd}           Tokj2874
${retour}
${retourr}
***Test Cases***
${retour}       valid login         ${VALID USER}       ${VALID PASSWORD}
${retourr}      invalid login       ${invalidlog}        ${VALID PASSWORD}
${retourr}      invalid login       ${VALID USER}        ${invalidpwd}
*** Keywords ***