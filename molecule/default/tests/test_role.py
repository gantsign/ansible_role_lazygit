def test_lazygit(host):
    assert host.run('lazygit -v').rc == 0
