'''

store
Save the value, after optionally converting it to a different type.
This is the default action taken if none is specified expliclity.

store_const
Save a value defined as part of the argument specification,
rather than a value that comes from the arguments being parsed.
This is typically used to implement command line flags that aren’t booleans.

store_true / store_false
Save the appropriate boolean value.
These actions are used to implement boolean switches.

append
Save the value to a list.
Multiple values are saved if the argument is repeated.

append_const
Save a value defined in the argument specification to a list.

version
Prints version details about the program and then exits.

'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='300',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print ('simple_value     =', results.simple_value)
print ('constant_value   =', results.constant_value)
print ('boolean_switch   =', results.boolean_switch)
print ('collection       =', results.collection)
print ('const_collection =', results.const_collection)
