*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  liisa  liisa333
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  liisa333
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  mo  momo3434
    Output Should Contain  Username must be atleast 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ville5  villezille7
    Output Should Contain  Username must contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  liisa  liisa4
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enought Password Containing Only letters
    Input Credentials  majava  kalevimajava
    Output Should Contain  Password cannot be only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command