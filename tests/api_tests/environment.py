def before_scenario(context, scenario):
    print(f"\nScenario: {scenario.name}\n")


def before_step(context, step):
    print(f"-> Start step: {step.name}")


def after_step(context, step):
    print(f"<- End step: {step.name} passed")


def after_scenario(context, scenario):
    print(f"'{scenario.name}' scenario has passed")
