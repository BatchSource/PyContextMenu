import os
import sys
import subprocess


class filemenu:
    def add(self, text: str=None, key_name: str=None, target_file: str=None, icon: str=None, use_async: str=False):
        """
        Add python program to file context menu.
        """
        if target_file == None: target_file = sys.argv[0]
        if text == None: text = 'Open with '+str(os.path.splitext(os.path.basename(target_file))[0])
        if key_name == None: key_name = text
        if sys.platform.lower().startswith('win'):
            if use_async: command = subprocess.Popen
            else: command = subprocess.call
            if icon != None:
                command(['powershell', 'start', 'cmd', f"'/c reg add HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')} /v \"Icon\" /t REG_SZ /d \"\\\"{icon}\\\",0 \" /f\'",
                '-verb', 'runAs', '-windowstyle', 'hidden'])
            else:
                command(['powershell', 'start', 'cmd', f"'/c reg add HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f\'",
                '-verb', 'runAs', '-windowstyle', 'hidden'])            
        else:
            raise OSError('Invalid operating system.')

    def remove(self, key_name: str=None, target_file: str=None, use_async=False):
        """
        Remove python program from file context menu.
        """
        if target_file == None: target_file = sys.argv[0]
        if key_name == None: key_name = 'Open with '+str(os.path.splitext(os.path.basename(target_file))[0])

        if sys.platform.lower().startswith('win'):
            if use_async: command = subprocess.Popen
            else: command = subprocess.call
            command(['powershell', 'start', 'cmd', f"'/c reg delete HKEY_CLASSES_ROOT\\*\\shell\\{key_name.replace(' ', '')} /f\'", '-verb', 'runAs', '-windowstyle', 'hidden'])
        else:
            raise OSError('Invalid operating system.')

class foldermenu:
    def add(self, text: str=None, key_name: str=None, target_file: str=None, icon: str=None, use_async: str=False):
        """
        Add python program to folder context menus.
        """
        if target_file == None: target_file = sys.argv[0]
        if text == None: text = 'Open with '+str(os.path.splitext(os.path.basename(target_file))[0])
        if key_name == None: key_name = text
        if sys.platform.lower().startswith('win'):
            if use_async: command = subprocess.Popen
            else: command = subprocess.call
            if icon != None:
                command(['powershell', 'start', 'cmd',
                f"'/c reg add HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')} /v \"Icon\" /t REG_SZ /d \"\\\"{icon}\\\",0 \" /f",

                f"&reg add HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')} /v \"Icon\" /t REG_SZ /d \"\\\"{icon}\\\",0 \" /f",

                f"&reg add HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')} /v \"Icon\" /t REG_SZ /d \"\\\"{icon}\\\",0 \" /f",

                f"&reg add HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')} /v \"Icon\" /t REG_SZ /d \"\\\"{icon}\\\",0 \" /f\'",

                '-verb', 'runAs', '-windowstyle', 'hidden'])
            else:
                command(['powershell', 'start', 'cmd',
                f"'/c reg add HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",

                f"&reg add HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",

                f"&reg add HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f",

                f"&reg add HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')} /ve /t REG_SZ /d \"{text}\" /f",
                f"&reg add HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')}\\command /ve /t REG_SZ /d \"\\\"{target_file}\\\" \\\"%1\\\"\" /f\'",

                '-verb', 'runAs', '-windowstyle', 'hidden'])
        else:
            raise OSError('Invalid operating system.')

    def remove(self, key_name: str=None, target_file: str=None, use_async=False):
        """
        Remove python program from folder context menus.
        """

        if target_file == None: target_file = sys.argv[0]
        if key_name == None: key_name = 'Open with '+str(os.path.splitext(os.path.basename(target_file))[0])

        if sys.platform.lower().startswith('win'):
            if use_async: command = subprocess.Popen
            else: command = subprocess.call
            command(['powershell', 'start', 'cmd',
            f"'/c reg delete HKEY_CLASSES_ROOT\\Directory\\shell\\{key_name.replace(' ', '')} /f",
            f"&reg delete HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\{key_name.replace(' ', '')} /f",
            f"&reg delete HKEY_CLASSES_ROOT\\Drive\\shell\\{key_name.replace(' ', '')} /f",
            f"&reg delete HKEY_CLASSES_ROOT\\LibraryFolder\\background\\shell\\{key_name.replace(' ', '')} /f\'",
            '-verb', 'runAs', '-windowstyle', 'hidden'])
        else:
            raise OSError('Invalid operating system.')