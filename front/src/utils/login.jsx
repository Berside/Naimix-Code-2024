import endpoints from './endpoints.jsx';
const baseUrl = endpoints();

export async function login(email, password) {
  try {
    const fullUrl = `${baseUrl}/api/v1/auth/login?email=${email}&password=${password}`;
    console.log(fullUrl);
    const response = await fetch(fullUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const result = await response.json();
    console.log('Success:', result);
    return result;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}


// import endpoints from './endpoints.jsx';
// const baseUrl = endpoints();

// export async function login(email, password) {
//   try {
//     const fullUrl = `${baseUrl}/api/v1/auth/login`;
    
//     // Send POST request instead of GET
//     const response = await fetch(fullUrl, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify({ email, password })
//     });

//     if (!response.ok) {
//       throw new Error(`HTTP error! status: ${response.status}`);
//     }

//     const result = await response.json();
//     console.log('Success:', result);
//     return result;
//   } catch (error) {
//     console.error('Error in login function:', error);
//     throw error;
//   }
// }
