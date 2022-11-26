import { createBottomTabNavigator } from "@react-navigation/bottom-tabs"
import { Index } from "../views/home"

const BottomTab = createBottomTabNavigator()

export default () => {
	return (
		<BottomTab.Navigator initialRouteName="Loading">
			<BottomTab.Screen name="home" component={Index} />
		</BottomTab.Navigator>
	)
}
