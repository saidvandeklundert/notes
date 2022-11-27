import gc

# Clean up what might be garbage so far.
gc.collect(2)
# Exclude current items from future GC.
gc.freeze()

allocs, gen1, gen2 = gc.get_threshold()
allocs = 50_000  # Start the GC sequence every 50K not 700 allocations.
gen1 = gen1 * 2
gen2 = gen2 * 2
gc.set_threshold(allocs, gen1, gen2)
