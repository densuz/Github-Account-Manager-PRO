; Git Account Manager Pro - NSIS Installer Script
; Creates a professional Windows installer with portable/installer options

!define APP_NAME "Git Account Manager Pro"
!define APP_VERSION "2.1.0"
!define APP_PUBLISHER "Git Account Manager Team"
!define APP_URL "https://github.com/densuz/Github-Account-Manager-PRO"
!define APP_EXECUTABLE "GitAccountManagerPro.exe"
!define APP_ICON "GitAccountManagerPro.exe"

; Modern UI
!include "MUI2.nsh"
!include "FileFunc.nsh"

; Installer Information
Name "${APP_NAME}"
OutFile "GitAccountManagerPro-Setup.exe"
InstallDir "$PROGRAMFILES\${APP_NAME}"
InstallDirRegKey HKLM "Software\${APP_NAME}" "Install_Dir"
RequestExecutionLevel admin

; Version Information
VIProductVersion "${APP_VERSION}.0"
VIAddVersionKey "ProductName" "${APP_NAME}"
VIAddVersionKey "ProductVersion" "${APP_VERSION}"
VIAddVersionKey "CompanyName" "${APP_PUBLISHER}"
VIAddVersionKey "FileVersion" "${APP_VERSION}"
VIAddVersionKey "FileDescription" "${APP_NAME} Installer"
VIAddVersionKey "LegalCopyright" "© 2025 ${APP_PUBLISHER}"

; Interface Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${APP_ICON}"
!define MUI_UNICON "${APP_ICON}"

; Welcome Page
!define MUI_WELCOMEPAGE_TITLE "Welcome to ${APP_NAME} Setup"
!define MUI_WELCOMEPAGE_TEXT "This wizard will guide you through the installation of ${APP_NAME} v${APP_VERSION}.$\r$\n$\r$\n${APP_NAME} is a professional Git account management tool with multi-language support.$\r$\n$\r$\nClick Next to continue."

; License Page
!define MUI_LICENSEPAGE_TEXT_TOP "Please review the license terms before installing ${APP_NAME}."
!define MUI_LICENSEPAGE_TEXT_BOTTOM "If you accept the terms of the agreement, click I Agree to continue. You must accept the agreement to install ${APP_NAME}."

; Components Page
!define MUI_COMPONENTSPAGE_TEXT_TOP "Choose the installation type for ${APP_NAME}. You can install it as a portable application or as a full system installation."

; Directory Page
!define MUI_DIRECTORYPAGE_TEXT_TOP "Setup will install ${APP_NAME} in the following folder. To install in a different folder, click Browse and select another folder. Click Next to continue."

; Instfiles Page
!define MUI_INSTFILESPAGE_FINISHHEADER_TEXT "Installation Complete"
!define MUI_INSTFILESPAGE_FINISHHEADER_SUBTEXT "Setup was completed successfully."

; Finish Page
!define MUI_FINISHPAGE_TITLE "Completing the ${APP_NAME} Setup Wizard"
!define MUI_FINISHPAGE_TEXT "${APP_NAME} has been installed on your computer.$\r$\n$\r$\nClick Finish to close this wizard."
!define MUI_FINISHPAGE_RUN "$INSTDIR\${APP_EXECUTABLE}"
!define MUI_FINISHPAGE_RUN_TEXT "Launch ${APP_NAME}"
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\README.md"
!define MUI_FINISHPAGE_SHOWREADME_TEXT "Show Release Notes"

; Uninstaller
!define MUI_UNWELCOMEPAGE_TITLE "Uninstall ${APP_NAME}"
!define MUI_UNWELCOMEPAGE_TEXT "This wizard will guide you through the uninstallation of ${APP_NAME}.$\r$\n$\r$\nClick Uninstall to start the uninstallation process."

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

; Installer Sections
Section "Core Application" SecCore
    SectionIn RO  ; Required section
    
    SetOutPath "$INSTDIR"
    
    ; Copy main files
    File "${APP_EXECUTABLE}"
    File "README.md"
    File "RELEASE_NOTES.md"
    File "VERSION.txt"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    
    ; Registry entries
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "DisplayName" "${APP_NAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "InstallLocation" "$INSTDIR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "DisplayVersion" "${APP_VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "Publisher" "${APP_PUBLISHER}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "URLInfoAbout" "${APP_URL}"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "NoRepair" 1
    
    ; Calculate size
    ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
    IntFmt $0 "0x%08X" $0
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "EstimatedSize" "$0"
SectionEnd

Section "Desktop Shortcut" SecDesktop
    CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${APP_EXECUTABLE}" "" "$INSTDIR\${APP_EXECUTABLE}" 0
SectionEnd

Section "Start Menu Shortcuts" SecStartMenu
    CreateDirectory "$SMPROGRAMS\${APP_NAME}"
    CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${APP_EXECUTABLE}" "" "$INSTDIR\${APP_EXECUTABLE}" 0
    CreateShortCut "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
SectionEnd

Section "Portable Mode" SecPortable
    ; Create portable launcher
    FileOpen $0 "$INSTDIR\run_portable.bat" w
    FileWrite $0 "@echo off$\r$\n"
    FileWrite $0 "cd /d \"$INSTDIR\"$\r$\n"
    FileWrite $0 "\"${APP_EXECUTABLE}\"$\r$\n"
    FileClose $0
    
    ; Create portable info file
    FileOpen $0 "$INSTDIR\PORTABLE.txt" w
    FileWrite $0 "Git Account Manager Pro - Portable Mode$\r$\n"
    FileWrite $0 "=====================================$\r$\n$\r$\n"
    FileWrite $0 "This is a portable installation of ${APP_NAME}.$\r$\n$\r$\n"
    FileWrite $0 "To run the application:$\r$\n"
    FileWrite $0 "1. Double-click ${APP_EXECUTABLE}$\r$\n"
    FileWrite $0 "2. Or run run_portable.bat$\r$\n$\r$\n"
    FileWrite $0 "To uninstall:$\r$\n"
    FileWrite $0 "Simply delete this folder.$\r$\n$\r$\n"
    FileWrite $0 "All settings and data are stored in the 'data' subfolder.$\r$\n"
    FileClose $0
SectionEnd

; Section Descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecCore} "Core application files required to run ${APP_NAME}."
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Create a shortcut on the desktop for easy access."
    !insertmacro MUI_DESCRIPTION_TEXT ${SecStartMenu} "Create shortcuts in the Start Menu Programs folder."
    !insertmacro MUI_DESCRIPTION_TEXT ${SecPortable} "Enable portable mode features for easy removal and portability."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; Uninstaller Section
Section "Uninstall"
    ; Remove files
    Delete "$INSTDIR\${APP_EXECUTABLE}"
    Delete "$INSTDIR\README.md"
    Delete "$INSTDIR\RELEASE_NOTES.md"
    Delete "$INSTDIR\VERSION.txt"
    Delete "$INSTDIR\run_portable.bat"
    Delete "$INSTDIR\PORTABLE.txt"
    Delete "$INSTDIR\Uninstall.exe"
    
    ; Remove shortcuts
    Delete "$DESKTOP\${APP_NAME}.lnk"
    Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
    Delete "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk"
    RMDir "$SMPROGRAMS\${APP_NAME}"
    
    ; Remove registry entries
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
    DeleteRegKey HKLM "Software\${APP_NAME}"
    
    ; Remove installation directory
    RMDir "$INSTDIR"
SectionEnd

; Functions
Function .onInit
    ; Check if already installed
    ReadRegStr $R0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "UninstallString"
    StrCmp $R0 "" done
    
    MessageBox MB_OKCANCEL|MB_ICONEXCLAMATION \
        "${APP_NAME} is already installed. $\n$\nClick 'OK' to remove the previous version or 'Cancel' to cancel this upgrade." \
        IDOK uninst
    Abort
    
    uninst:
        ClearErrors
        ExecWait '$R0 _?=$INSTDIR'
        
        IfErrors no_remove_uninstaller done
        no_remove_uninstaller:
    
    done:
FunctionEnd

Function .onInstSuccess
    ; Show success message
    MessageBox MB_YESNO|MB_ICONQUESTION \
        "Installation completed successfully!$\n$\nWould you like to launch ${APP_NAME} now?" \
        IDYES launch IDNO done
    
    launch:
        Exec "$INSTDIR\${APP_EXECUTABLE}"
    
    done:
FunctionEnd
