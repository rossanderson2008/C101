import dropbox

class TransferData:
    def __inif__ (self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BGFGMerfpPyJ06uQaw8SWH-6lFMEuybX-hYqXTQN_VdTNwK-1PMOAN-4f8NRltMleng9yD25wTUfMq71K8LsxjTm-xfVCErNMz9xFV2jT0V7jfZhb6zP8m5ICNoo32fTDHgxIjdCHSAm'
    transferData=TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from,file_to)
    print("file has been moved!!!")

#if __name__== '__main__':
main()
