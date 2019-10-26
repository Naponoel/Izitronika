from optparse import OptionParser
import func

parser = OptionParser()

parser.add_option('-u', action='store', type='string', dest='username')
parser.add_option('-p', action='store', type='string', dest='passw')

(options, args) = parser.parse_args()

main = func.Anketa(options.username, options.passw)
main.login()
main.crunch_time()
