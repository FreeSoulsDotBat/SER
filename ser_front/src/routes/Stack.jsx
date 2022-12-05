import { createNativeStackNavigator } from "@react-navigation/native-stack"
import { Login } from "../views/auth/Login"
import { PassRecovery } from "../views/auth/PassRecovery"

const Stack = createNativeStackNavigator()

export default () => {
	return (
		<Stack.Navigator initialRouteName="Test">
			<Stack.Screen
				name="Test"
				component={PassRecovery}
				options={{ headerShown: false }}
			/>
		</Stack.Navigator>
	)
}
