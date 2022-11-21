import { createNativeStackNavigator } from '@react-navigation/native-stack'
import { Header } from '../components/Header'
import { Opening } from '../views/common/Opening'
import { Index } from '../views/home'

const Stack = createNativeStackNavigator()

export default () => {
	return (
		<Stack.Navigator initialRouteName="Opening">
			<Stack.Screen
				name="Opening"
				component={Opening}
				options={{ headerShown: false }}
			/>
			<Stack.Screen
				name="Home"
				component={Index}
				options={{
					header: () => <Header />,
				}}
			/>
		</Stack.Navigator>
	)
}
