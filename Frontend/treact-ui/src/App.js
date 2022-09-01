import "tailwindcss/dist/base.css";
import "styles/globalStyles.css";
import React from "react";
import PostList from './posts/postlist';
import Login from "./accounts/login";
import Signup from "./accounts/signup";
import CreatePost from "./posts/new";
import { css } from "styled-components/macro"; //eslint-disable-line

import Header from "./components/headers/light.js";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import PrivateRoute from "./utils/PrivateRoute";
import { AuthProvider } from "./context/AuthContext";


export default function App() {
  // If you want to disable the animation just use the disabled `prop` like below on your page's component
  // return <AnimationRevealPage disabled>xxxxxxxxxx</AnimationRevealPage>;


  return (
      
      <Router>
        <AuthProvider>
          <Header />
          <Switch>
            <PrivateRoute exact path="/posts/create">
              <CreatePost />
            </PrivateRoute>
            <Route path="/accounts/login">
              <Login />
            </Route>
            <Route path="/accounts/signup">
              <Signup />
            </Route>
            <Route path="/">
              <PostList />
            </Route>
          </Switch>
        </AuthProvider>
      </Router>
  );
}

// export default EventLandingPage;
// export default HotelTravelLandingPage;
// export default AgencyLandingPage;
// export default SaaSProductLandingPage;
// export default RestaurantLandingPage;
// export default ServiceLandingPage;
// export default HostingCloudLandingPage;

// export default LoginPage;
// export default SignupPage;
// export default PricingPage;
// export default AboutUsPage;
// export default ContactUsPage;
// export default BlogIndexPage;
// export default TermsOfServicePage;
// export default PrivacyPolicyPage;

// export default MainLandingPage;
