import sys
import zoo_model
import zoo_command

#model = zoo_model.ZooModel()
# model.initModel('srv8-pingnie:2181')

command = zoo_command.ZooCommand('127.0.0.1>createee')
if(command.error):
    print(command.error)
