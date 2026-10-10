# interactor-dress-designer-maskscore

Scripts that sample garments from a second-hand fashion dataset and drive a pattern-drafting garment simulator to rebuild them as USD.

## What it is for

It is the start of a pipeline for building MaskScore and EditScore datasets from real garments.
One script samples garment records from the dataset's parquet, and two run inside the simulator's
scripting host to import a reference image and export the garment as a USD file. The scoring step
is not part of it.

## Run

`python dataset_sampler.py` reads the dataset from its workspace checkout. The other two scripts
run from the simulator's own scripting console.

## Licence

MIT. See [LICENSE](LICENSE).
