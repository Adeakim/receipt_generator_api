// import NavBar from './NavBar';
// import Home from './Home';
import {BrowserRouter as Router,Route,Switch} from "react-router-dom";
import Create from './Create';
import Register from './Register';
// import BlogDetails from './BlogDetails';
// import NotFound from './NotFound';

function App() {
  return (
    <Router>
      <div className="App">
    <div className="content">
     <Switch>
       {/* <Route exact path="/"> <Home /></Route> */}
       <Route path="/create"> <Create/></Route>
       <Route path="/signup"> <Register/></Route>
       {/* <Route path="*"> <NotFound /> </Route> */}
     </Switch>
    </div>
    </div>
    </Router>
    
  );
}

export default App;
