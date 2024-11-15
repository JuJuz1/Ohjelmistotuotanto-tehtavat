*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    New Credentials  testaus  testiUusi12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    New Credentials  testi  AsP12561!"¤&
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    New Credentials  te  AsP12561!"¤&
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    New Credentials  testi123  AsP12561!"¤&
    Output Should Contain  Only characters a-z are allowed

Register With Valid Username And Too Short Password
    New Credentials  testaus  A2
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    New Credentials  testaus  AsPLidaWIx
    Output Should Contain  Password must contain at least 1 special character

*** Keywords ***
Create User And Input New Command
    Create User  testi  testaaja16
    Input New Command