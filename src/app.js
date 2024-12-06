import React, { useState, useEffect } from 'react';
import axios from 'axios';
import SearchResults from './SearchResults';
import BlogPage from './BlogPage'; // Add this import

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(`http://localhost:5000/api/search?query=${query}`);
      setResults(response.data);
    };
    fetchData();
  }, [query]);

  const handleSearch = (e) => {
    setQuery(e.target.value);
  };

  return (
    <div>
      <input type="text" value={query} onChange={handleSearch} />
      <button onClick={() => setQuery(query)}>Search</button>
      {results.length > 0 && <SearchResults results={results} />}
      <BlogPage /> // Add this line
    </div>
  );
}

export default App;
