import endpoints from './endpoints.jsx';
const baseUrl = endpoints();
export async function Prof(token) {
  try {
    const fullUrl = `${baseUrl}/api/v1/user/auth/get_current_user/`;
    const response = await fetch(fullUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
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