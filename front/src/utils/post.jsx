import endpoints from './endpoints.jsx';
const baseUrl = endpoints();

export async function post(data) {
  try {
    const response = await fetch(`${baseUrl}/api/v1/auth/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log('Success:', result);
    return result;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Example usage:
const userData = {
  email: 'example@email.com',
  password: 'securePassword123',
  birthdate: '1990-01-01',
  birth_country: 'USA',
  birth_city: 'New York',
  first_name: 'John',
  last_name: 'Doe',
  middle_name: '',
  telephone: '1234567890'
};

post(userData)
  .then(result => console.log(result))
  .catch(error => console.error(error));
