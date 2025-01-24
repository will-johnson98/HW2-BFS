# write tests for bfs
import pytest
from search.graph import Graph

def test_bfs_traversal():
    """Test BFS traversal on tiny network"""
    g = Graph("data/tiny_network.adjlist")
    
    # Test traversal from Nevan Krogan
    traversal = g.bfs("Nevan Krogan")
    assert len(traversal) == 30  # Verify all nodes visited
    assert traversal[0] == "Nevan Krogan"  # Start node first
    
    # Test first few nodes are immediate neighbors
    neighbors = {"34272374", "32353859", "30944313"}
    assert set(traversal[1:4]) == neighbors
    
    # Test traversal from different start node
    traversal2 = g.bfs("Marina Sirota") 
    assert len(traversal2) == 30
    assert traversal2[0] == "Marina Sirota"

def test_bfs_pathfinding():
    """Test BFS pathfinding on citation network"""
    g = Graph("data/citation_network.adjlist")
    
    # Test path between connected nodes
    # Finding path from Charles Chiu to Steven Altschuler
    path = g.bfs("Charles Chiu", "Steven Altschuler")
    assert path is not None
    assert path[0] == "Charles Chiu"
    assert path[-1] == "Steven Altschuler"
    
    # Test path between same node
    path = g.bfs("Marina Sirota", "Marina Sirota")
    assert path is None
    
    # Test path between unconnected nodes
    # Using a PMID that doesn't connect to faculty
    path = g.bfs("34272374", "invalid_node")
    assert path is None

def test_invalid_start():
    """Test BFS with invalid start node"""
    g = Graph("data/tiny_network.adjlist")
    result = g.bfs("NonexistentNode", "Steven Altschuler")
    assert result is None


def test_invalid_end():
    """Test BFS with invalid start node"""
    g = Graph("data/tiny_network.adjlist")
    result = g.bfs("Steven Altschuler", "NonexistentNode")
    assert result is None

def test_tiny_specific_paths():
    """Test specific known paths in tiny network"""
    g = Graph("data/tiny_network.adjlist")
    
    # Test path from Luke Gilbert to Atul Butte
    path = g.bfs("Luke Gilbert", "Atul Butte")
    assert path is not None
    assert path[0] == "Luke Gilbert"
    assert path[-1] == "Atul Butte"
    
    # Verify path length is optimal
    # One possible shortest path: Luke Gilbert -> Martin Kampmann -> Nevan Krogan -> Marina Sirota -> Atul Butte
    assert len(path) <= 5

def test_citation_network_properties():
    """Test properties of citation network"""
    g = Graph("data/citation_network.adjlist")
    
    # Test path between papers
    path = g.bfs("34272374", "32353859")  # PMIDs from tiny network
    assert path is not None
    assert path[0] == "34272374"
    assert path[-1] == "32353859"

    # Test traversal from faculty member
    traversal = g.bfs("Nevan Krogan")
    print(f"Traversal Length: {len(traversal)}")
    assert len(traversal) == 5120, "Incorrect `len(traversal)`" # This should raise an error, because the traversal from N.K. does not reach all nodes (only 5044)

