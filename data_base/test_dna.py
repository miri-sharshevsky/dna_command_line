from data_base.dna import DNA


def test_dna():
    a = DNA("AGC")
    b = DNA("GGC")
    c = DNA("AGC")
    assert a == c
    assert a != b
    assert len(a) == 3
    a.insert('S', 1)
    b.assignment(a)
    assert a == b
    print(a)


if __name__ == '__main__':
    test_dna()
