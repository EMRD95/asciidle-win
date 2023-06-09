; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Asciidle"
#define MyAppVersion "1.0"
#define MyAppPublisher "EMRD95"
#define MyAppURL "https://github.com/EMRD95/asciidle-win"
#define MyAppExeName "asciidle.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{5CEFAD0D-32FC-436B-AB6F-01736F7C8335}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\LICENCE
InfoBeforeFile=C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\before-installation-message.txt
InfoAfterFile=C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\after-installation-message.txt
PrivilegesRequired=lowest
OutputBaseFilename=Asciidle_Setup
SetupIconFile=C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\res\asciidle.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\asciidle.cf"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\asciidle-config.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\download-ascii-art.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\download-ascii-art2.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\LICENCE"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\txt\*"; DestDir: "{app}\txt"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\res\*"; DestDir: "{app}\res"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Downloads\asciidle-win-main2\asciidle-win-main\res\admin_shield.png"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autoprograms}\{#MyAppName}\{#MyAppName} Configuration"; Filename: "{app}\asciidle-config.exe"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{autodesktop}\{#MyAppName} Configuration"; Filename: "{app}\asciidle-config.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
; Filename: "{app}\asciidle.exe"; Parameters: """{app}\asciidle.cf"""; Flags: runhidden nowait postinstall

[Code]
procedure UpdateConfigFile(ADestPath: string);
var
  ConfigFile: string;
  ConfigLines: TStrings;
  i: Integer;
begin
  ConfigFile := ADestPath + '\asciidle.cf';
  ConfigLines := TStringList.Create;
  try
    ConfigLines.LoadFromFile(ConfigFile);
    for i := 0 to ConfigLines.Count - 1 do
    begin
      if Pos('# Path for the ASCII art txt files', ConfigLines[i]) > 0 then
      begin
        ConfigLines[i + 1] := ADestPath + '\txt';
        Break;
      end;
    end;
    ConfigLines.SaveToFile(ConfigFile);
  finally
    ConfigLines.Free;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
    UpdateConfigFile(ExpandConstant('{app}'));
end;


