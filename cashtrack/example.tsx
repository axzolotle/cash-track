import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Cash Track</Text>
      <View style={styles.card}>
        <Text>Total Balance</Text>
        <Text style={styles.amount}>$2.00</Text>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 16,
  },
  text: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  card:{
    backgroundColor: 'white',
    padding: 16,
    borderRadius: 8,
    shadowColor: '#000',
  },
  amount:{
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 8,
  }
});
