import React, { useState, useEffect } from 'react';
import { View, Text, Button, Share } from 'react-native';

const App = () => {
  const [quote, setQuote] = useState('');

  const fetchRandomQuote = async () => {
    try {
      const response = await fetch('YOUR_API_ENDPOINT');
      const data = await response.json();
      const randomQuote = data[Math.floor(Math.random() * data.length)];
      setQuote(randomQuote);
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const shareQuote = async () => {
    try {
      await Share.share({
        message: `"${quote.text}" - ${quote.author}`,
      });
    } catch (error) {
      console.error('Error sharing quote:', error);
    }
  };

  useEffect(() => {
    fetchRandomQuote();
  }, []);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 20, marginBottom: 20, textAlign: 'center' }}>{quote.text}</Text>
      <Text style={{ fontSize: 16, fontStyle: 'italic' }}>- {quote.author}</Text>
      <View style={{ marginTop: 20 }}>
        <Button title="Share Quote" onPress={shareQuote} />
        <Button title="Next Quote" onPress={fetchRandomQuote} />
      </View>
    </View>
  );
};

export default App;

