import { createNativeStackNavigator } from "@react-navigation/native-stack"
import { Login } from "../views/auth/Login"

const Stack = createNativeStackNavigator()

export default () => {
	return (
		<Stack.Navigator initialRouteName="Login">
			<Stack.Screen
				name="Login"
				component={Login}
				options={{ headerShown: false }}
			/>
		</Stack.Navigator>
	)
}
