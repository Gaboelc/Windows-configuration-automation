import subprocess

class programs:
    
    def __init__(self):
        self.programs = ['winrar', 'googlechrome', 'firefox','vscode', 'arduino',
                         'nodejs', 'mongodb', 'mongodb-compass-community', 'python',
                         'anaconda3', 'notepadplusplus', 'r', 'r.studio', 'winscp',
                         'steam-client', 'inkscape', 'obs-studio', 'telegram', 'putty',
                         'dia', 'mobaxterm', 'brave', 'discord', 'epicgameslauncher',
                         'qbittorrent', 'git', 'powerbi', 'netbeans', 'spotify']
    
    def run_process(self, command):
        subprocess.run(['powershell', '-Command', command])
        
    def change_execution_policy(self):
        print('''
              --------------------------------------------------------
              The execution policies will be changed to 'RemoteSigned'
              --------------------------------------------------------
              ''')
        
        self.run_process('Set-ExecutionPolicy RemoteSigned -scope CurrentUser')
        self.run_process('Get-ExecutionPolicy -List')
        
    def install_chocolatey(self):
        print('''
              --------------------------------------------------------
                            Chocolatey will be installed
              --------------------------------------------------------
              ''')
        self.run_process('[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://community.chocolatey.org/install.ps1"))')
        self.run_process('choco feature enable -n allowGlobalConfirmation -y')
        
        print('''
              --------------------------------------------------------
                                Chocolatey Installed
              --------------------------------------------------------
              ''')
        
        self.run_process('Start-Sleep -s 2')
        
        
    def install_programs(self):
        for i in self.programs:
            
            self.run_process(f'choco install {i}')