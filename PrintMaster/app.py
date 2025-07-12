"""
Entry point for the PrintMaster project.

Running this script executes the `run()` function in every module
so you can see all print‑expression examples in one go.
"""

import arithmetic_prints as ar
import logical_prints as lo
import string_prints as st
import collections_prints as co
import loop_prints as lp
import function_prints as fu
import misc_prints as mi
def run():
    print("=== PrintMaster Demo === \n")
    ar.run()
    lo.run()
    st.run()
    co.run()
    lp.run()
    fu.run()
    mi.run()
    print("=== End of Demo ===")

if __name__ == "__main__":
    run()

