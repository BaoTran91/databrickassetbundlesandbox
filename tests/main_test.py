from datakickstart_dabs import main


def test_load_top_artists_by_year():
    taxis = main.load_top_artists_by_year()
    assert taxis.count() > 5
