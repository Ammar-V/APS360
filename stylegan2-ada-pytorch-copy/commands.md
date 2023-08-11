### Style mixing

python style_mixing.py --network ./~/training-runs/00002-styledata-auto1/network-snapshot-000800.pkl --rows 0-10 --cols 10-20 --noise-mode const --outdir test_styles

python projector.py --network ./~/training-runs/00002-styledata-auto1/network-snapshot-000800.pkl --target ./good_birds/2/frame_0000.jpg --outdir ./good_birds/2