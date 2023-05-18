# Run the USGS streamgage data scraping script on all 50 states and Washington, D.C.

state_codes="al ak az ar ca co ct de dc fl ga hi id il in ia ks ky la me md ma mi mn ms mo mt ne nv nh nj nm ny nc nd oh ok or pa ri sc sd tn tx ut vt va wa wv wi wy"

for state in $state_codes
do
    python3 get_streamgages_for_state.py $state
done