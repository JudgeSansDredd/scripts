#!/usr/bin/env bash

# This script is set up for laravel 9, which requires php 8.1
brew install php@8.1
brew unlink php
brew link --overwrite php@8.1

###################################################
# Get some information about the current terminal #
###################################################
LINES=$(($(tput lines) - 10))
COLS=$(($(tput cols) - 10))
GREEN=$(tput setaf 2)
DEFAULT=$(tput sgr0)

##################################
# Where do you want your project #
##################################
if [ -z "$1" ];then
    PROJECTNAME=$(whiptail --inputbox "What is the project name?" $LINES $COLS --title "Create Laravel React Application" 3>&1 1>&2 2>&3)
    exitstatus=$?
    if [ $exitstatus -ne 0 ]; then
        exit 0;
    fi
else
    PROJECTNAME=$1
fi

##############################
# Create directory variables #
##############################
CURRENTDIR=$(pwd)
PROJECTPATH="$CURRENTDIR/$PROJECTNAME"
DATABASEPATH="$PROJECTPATH/database/database.sqlite"
ENVPATH="$PROJECTPATH/.env"
TAILWINDCONFIGPATH="$PROJECTPATH/tailwind.config.js"
APPBLADEPATH="$PROJECTPATH/resources/views/app.blade.php"
VITECONFIGPATH="$PROJECTPATH/vite.config.js"

##########################
# Create laravel project #
##########################
composer create-project --prefer-dist laravel/laravel $PROJECTNAME
cd $PROJECTPATH

################################################
# Update the env with app name and sqlite cnxn #
################################################
sed -i '' "s/^APP_NAME=Laravel$/APP_NAME=\"$PROJECTNAME\"/g" $ENVPATH
sed -i '' 's/^DB_CONNECTION=mysql$/DB_CONNECTION=sqlite/g' $ENVPATH
sed -i '' '/^DB_HOST/d' $ENVPATH
sed -i '' '/^DB_PORT/d' $ENVPATH
sed -i '' "s/^DB_DATABASE=laravel$/DB_DATABASE=$DATABASEPATH/g" $ENVPATH
sed -i '' '/^DB_USERNAME/d' $ENVPATH
sed -i '' '/^DB_PASSWORD/d' $ENVPATH

#######################################
# Require breeze (API authentication) #
#######################################
composer require laravel/breeze --dev

###########################################
# Install breeze authentication for react #
###########################################
php artisan breeze:install react

########################
# Install npm packages #
########################
npm i --save-dev @types/react-dom typescript ts-node @types/react flowbite
npm install

###########
# Migrate #
###########
php artisan migrate --force

########################
# Remove welcome blade #
########################
rm $PROJECTPATH/resources/views/welcome.blade.php

#######################
# Initiate typescript #
#######################
npx tsc --init --jsx react

################################################
# Update tailwind to look for ts and tsx files #
################################################
sed -i '' "s/\.js/\.ts/g" $TAILWINDCONFIGPATH

###################################
# Update tailwind to use flowbite #
###################################
echo -e "import flowbite from 'flowbite';\n$(cat $TAILWINDCONFIGPATH)" > $TAILWINDCONFIGPATH
sed -i '' "s/\[forms\]/[forms, flowbite]/" $TAILWINDCONFIGPATH

############################################
# Update app.blade.php to look for app.tsx #
############################################
sed -i '' "s/\.js/\.ts/g" $APPBLADEPATH

##########################################
# Update vite.config to look for app.tsx #
##########################################
sed -i '' "s/\.js/\.ts/g" $VITECONFIGPATH

###########################
# Rename jsx files as tsx #
###########################
for file in $PROJECTPATH/resources/js/*.jsx; do
    mv -- "$file" "${file%.jsx}.tsx"
    sed -i '' "s/\.js/\.ts/g" "${file%.jsx}.tsx"
done
# Components, Layouts, and Pages
for file in $PROJECTPATH/resources/js/Components/*.jsx; do
    mv -- "$file" "${file%.jsx}.tsx"
    sed -i '' "s/\.js/\.ts/g" "${file%.jsx}.tsx"
done
for file in $PROJECTPATH/resources/js/Layouts/*.jsx; do
    mv -- "$file" "${file%.jsx}.tsx"
    sed -i '' "s/\.js/\.ts/g" "${file%.jsx}.tsx"
done
for file in $PROJECTPATH/resources/js/Pages/*.jsx; do
    mv -- "$file" "${file%.jsx}.tsx"
    sed -i '' "s/\.js/\.ts/g" "${file%.jsx}.tsx"
done
for file in $PROJECTPATH/resources/js/Pages/Auth/*.jsx; do
    mv -- "$file" "${file%.jsx}.tsx"
    sed -i '' "s/\.js/\.ts/g" "${file%.jsx}.tsx"
done

##################################
# Initialize as a git repository #
##################################
git init -b main
git add .
git commit -m "Big Bang"

printf "\nRun ${GREEN}php artisan serve${DEFAULT} to serve the website\n\n"
printf "Run ${GREEN}npm run dev${DEFAULT} to compile and watch the javascript\n\n"
