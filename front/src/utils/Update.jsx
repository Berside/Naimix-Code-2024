import endpoints from './endpoints.jsx';
const baseUrl = endpoints();
export async function Upda(Token, data) {
  try {
    const fullUrl = `${baseUrl}/api/v1/user/update/`;
    const response = await fetch(fullUrl, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${Token}`,
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}