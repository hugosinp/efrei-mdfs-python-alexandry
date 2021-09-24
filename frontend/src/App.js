import Header from './components/Header'
import Footer from './components/Footer'
import{ BrowserRouter as Router, Route } from 'react-router-dom'

import HomeScreen from './screens/HomeScreen'
import BookScreen from './screens/BookScreen';

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Route path='/' component={HomeScreen} exact />
        <Route path='/books/:id' component={BookScreen} />
      </main>
      <Footer />
    </Router>
  );
}

export default App;
