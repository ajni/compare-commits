import pytest
import requests.exceptions

import cc


def test_compareCommits_Raw():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", raw=True)
    assert data["base_commit"]["sha"] == "f6fcf385c9fd0df2ad666bc7765c127bd5e1528d"


def test_compareCommits():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable")
    assert len(data) == 30
    assert data[29] == "Merge pull request #1870 from spicyj/gh-1866"


# not nice to their server

# def test_handles_high_per_page():
#     # it does
#     data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", per_page=999999)
#     assert len(data) == 599


# def test_handles_negative_per_page():
#     # API seems to default to 250 results even though it specifies 30
#     data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", per_page=-3)
#     assert len(data) == 30


def test_fails_with_bad_owner():
    with pytest.raises(requests.exceptions.HTTPError):
        cc.compareCommits("kjsndhilsndjvf", "react", "0.11-stable", "0.12-stable")


def test_fails_with_bad_repo():
    with pytest.raises(requests.exceptions.HTTPError):
        cc.compareCommits("facebook", "kjsndhilsndjvf", "0.11-stable", "0.12-stable")


def test_fails_with_bad_base():
    with pytest.raises(requests.exceptions.HTTPError):
        cc.compareCommits("facebook", "react", "kjsndhilsndjvf", "0.12-stable")


def test_fails_with_bad_head():
    with pytest.raises(requests.exceptions.HTTPError):
        cc.compareCommits("facebook", "react", "0.11-stable", "kjsndhilsndjvf")


def test_matching_base_and_head():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.11-stable")
    assert len(data) == 0


def test_older_head_than_base():
    data = cc.compareCommits("facebook", "react", "0.12-stable", "0.11-stable")
    assert len(data) == 30
    assert data[29] == "update background color for image"


def test_fails_with_invalid_baseurl():
    with pytest.raises(requests.exceptions.InvalidURL):
        cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", baseurl="https:kjsndhilsndjvf")


def test_fails_with_wrong_baseurl():
    with pytest.raises(requests.exceptions.ConnectionError):
        cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", baseurl="https://kjsndhilsndjvf.example.com:9833")


def test_fails_with_bad_token():
    with pytest.raises(requests.exceptions.HTTPError):
        cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", token="kjsndhilsndjvf")


def test_compareCommits_per_page():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", per_page=20)
    assert len(data) == 20
    assert data[19] == "Update 2014-07-17-react-v0.11.md"


def test_compareCommits_page_2():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", page=2, per_page=20)
    assert len(data) == 20
    assert data[9] == "Merge pull request #1870 from spicyj/gh-1866"


def test_handles_high_page():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", page=999999)
    assert len(data) == 0


def test_ignores_negative_page():
    data = cc.compareCommits("facebook", "react", "0.11-stable", "0.12-stable", page=-3)
    assert len(data) == 30
    assert data[29] == "Merge pull request #1870 from spicyj/gh-1866"
