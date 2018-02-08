import firebase from 'firebase'

const config = {
    apiKey: "AIzaSyAQrupJZEA_LVTmTAYA5hsZXXevBkq0UgM",
    authDomain: "fun-food-friends-d1c7c.firebaseapp.com",
    databaseURL: "https://fun-food-friends-d1c7c.firebaseio.com",
    projectId: "fun-food-friends-d1c7c",
    storageBucket: "",
    messagingSenderId: "713524066738"
  };
  firebase.initializeApp(config);

  export default firebase;